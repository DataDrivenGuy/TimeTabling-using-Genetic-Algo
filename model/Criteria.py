from .Constant import Constant


# Reads configuration file and stores parsed objects
class Criteria:
    weights = [0, 0, 0, 0, 0, 0, 0]

    # check for room overlapping of classes
    @staticmethod
    def isRoomOverlapped(cc, slots, reservation, dur):
        if cc.room_type == "Y1":
            return False
        else:
            reservation_index = hash(reservation)
            cls = slots[reservation_index: reservation_index + dur]
            return any(True for slot in cls if len(slot) > 1)

    # does current room have enough seats
    @staticmethod
    def isSeatEnough(r, cc):
        return r.NumberOfSeats >= cc.NumberOfSeats

    # does current room have same type of room required
    @staticmethod
    def isComputerEnough(r, cc):
        return cc.room_type==r.room_type

    # check overlapping of classes for professors and student groups
    @staticmethod
    def isOverlappedProfStudentGrp(slots, cc, numberOfRooms, timeId):
        po = go = False

        dur = cc.Duration
        for i in range(numberOfRooms, 0, -1):
            # for each hour of class
            for j in range(timeId, timeId + dur):
                cl = slots[j]
                for cc1 in cl:
                    if cc != cc1:
                        # professor overlaps?
                        if not po and cc.professorOverlaps(cc1):
                            po = True
                        # student group overlaps?
                        if not go and cc.groupsOverlap(cc1):
                            go = True
                        # both type of overlapping? no need to check more
                        if po and go:
                            return po, go

            timeId += Constant.DAY_HOURS
        return po, go
    
    @staticmethod
    def isOverlappedLunch(time, dur):
        if (time in (10,11)) or ((time + dur - 1) in (10,11)) or ((time < 10) and (time + dur -1 > 10)):
            return True
        else:    
            return False

    @staticmethod
    def isOnlineClassMonday(day, cc):
        if cc.room_type == "Y1":
            if day == 0:
                return True
            else:
                return False
        else:
            if day == 0:
                return False
            else:
                return True
            
    @staticmethod
    def isOverlappedFlagCeremony(day, time):
        if (day == 2)  & (time==0):
            return True
        else:    
            return False
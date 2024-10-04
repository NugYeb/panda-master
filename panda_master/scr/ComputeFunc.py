from VGLN import Constant as con

class ComputeFunc():

    def __init__(self) -> None:
        self.cutx = con.CUTx

    def RightLeft_on_wall(self, objc_wid, ndvo) -> list:
        cutx = self.cutx
        tempwid = objc_wid - ndvo

        rightlift = [cutx[0]-(tempwid), 
                cutx[1]+cutx[0]-ndvo, 
                cutx[0]+cutx[1]+cutx[2]-tempwid, 
                cutx[0]+cutx[1]+cutx[2]+cutx[3]-ndvo, 
                cutx[0]+cutx[1]+cutx[2]+cutx[3]+cutx[4]-tempwid, 
                cutx[0]+cutx[1]+cutx[2]+cutx[3]+cutx[4]+cutx[5]-ndvo, 
                ]
        
        return rightlift


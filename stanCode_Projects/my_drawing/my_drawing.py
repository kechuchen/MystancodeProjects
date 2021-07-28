"""
File: my_drawing
Name:kechuchen
----------------------
TODO:Drawing of Kobe Bryant.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLine, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO:drawing
    """
    window = GWindow(width=680, height=778, title="Kobe")

    label = GLabel("\"THE MOST IMPORTANT ", x=40,y=50)
    label2 = GLabel("THING IS TO TRY AND ",x=40,y=80)
    label3 = GLabel("INSPIRE PEOPLE SO THAT ",x=40,y=110)
    label4 = GLabel("THEY CAN BE GREATER IN ",x=40,y=140)
    label5 = GLabel("WHATEVER THEY WANT TO", x=40, y=170)
    label6 = GLabel("DO.\"", x=40, y=200)
    label7 = GLabel("                                    ---Kobe Bryant", x=40, y=230)
    label8 = GLabel("stanCode SC101", x=40, y=750)
    label.font = 'Times New Roman-20-bold'
    label2.font = 'Times New Roman-20-bold'
    label3.font = 'Times New Roman-20-bold'
    label4.font = 'Times New Roman-20-bold'
    label5.font = 'Times New Roman-20-bold'
    label6.font = 'Times New Roman-20-bold'
    label6.font = 'Times New Roman-20-bold'
    label7.font = 'Times New Roman-15-bold'
    label8.font = 'Times New Roman-15-bold'
    window.add(label)
    window.add(label2)
    window.add(label3)
    window.add(label4)
    window.add(label5)
    window.add(label6)
    window.add(label7)
    window.add(label8)


    # LEFT ARM
    arm = GPolygon()
    # arm.filled = True
    arm.color = "black"
    arm.add_vertex((0, 349))
    arm.add_vertex((45, 352))
    arm.add_vertex((56, 347))
    arm.add_vertex((74, 348))
    arm.add_vertex((112, 339))
    arm.add_vertex((134, 333))
    arm.add_vertex((153, 325))
    arm.add_vertex((175, 321))
    arm.add_vertex((216, 299))
    arm.add_vertex((233, 296))
    arm.add_vertex((292, 270))
    arm.add_vertex((306, 258))
    arm.add_vertex((310, 250))
    arm.add_vertex((316, 246))
    arm.add_vertex((324, 243))
    arm.add_vertex((333, 240))
    arm.add_vertex((345, 236))
    arm.add_vertex((350, 233))
    arm.add_vertex((358, 233))
    arm.add_vertex((362, 233))
    arm.add_vertex((367, 235))
    arm.add_vertex((377, 240))
    arm.add_vertex((388, 247))
    arm.add_vertex((396, 251))
    arm.add_vertex((411, 286))
    arm.add_vertex((419, 308))
    arm.add_vertex((418, 320))
    arm.add_vertex((415, 325))
    arm.add_vertex((414, 326))
    arm.add_vertex((407, 330))
    arm.add_vertex((394, 332))
    arm.add_vertex((375, 332))
    arm.add_vertex((362, 328))
    arm.add_vertex((352, 323))
    arm.add_vertex((340, 318))
    arm.add_vertex((332, 312))
    arm.add_vertex((326, 303))
    arm.add_vertex((302, 321))
    arm.add_vertex((267, 333))
    arm.add_vertex((257, 336))
    arm.add_vertex((242, 339))
    arm.add_vertex((219, 349))
    arm.add_vertex((204, 356))
    arm.add_vertex((179, 365))
    arm.add_vertex((158, 368))
    arm.add_vertex((133, 370))
    arm.add_vertex((125, 369))
    arm.add_vertex((116, 364))
    arm.add_vertex((80, 375))
    arm.add_vertex((61, 378))
    arm.add_vertex((55, 380))
    arm.add_vertex((45, 384))
    arm.add_vertex((27, 398))
    arm.add_vertex((24, 397))
    arm.add_vertex((23, 395))
    arm.add_vertex((22, 393))
    arm.add_vertex((38, 381))
    arm.add_vertex((36, 378))
    arm.add_vertex((16, 385))
    arm.add_vertex((9, 383))
    arm.add_vertex((5, 379))
    arm.add_vertex((7, 374))
    arm.add_vertex((16, 373))
    arm.add_vertex((22, 370))
    arm.add_vertex((0, 357))
    window.add(arm)



    #left arm spot
    arm2 = GPolygon()
    arm2.add_vertex((419, 308))
    arm2.add_vertex((418, 320))
    arm2.add_vertex((415, 325))
    arm2.add_vertex((414, 326))
    arm2.add_vertex((407, 330))
    arm2.add_vertex((394, 332))
    arm2.add_vertex((375, 332))
    arm2.add_vertex((362, 328))
    arm2.add_vertex((352, 323))
    arm2.add_vertex((340, 318))
    arm2.add_vertex((332, 312))
    arm2.add_vertex((326, 303))
    arm2.add_vertex((302, 321))
    arm2.add_vertex((267, 333))
    arm2.add_vertex((257, 336))
    arm2.add_vertex((242, 339))
    arm2.add_vertex((219, 349))
    arm2.add_vertex((204, 356))
    arm2.add_vertex((179, 365))
    arm2.add_vertex((158, 368))
    arm2.add_vertex((133, 370))
    arm2.add_vertex((125, 369))
    arm2.add_vertex((116, 364))
    arm2.add_vertex((80, 375))
    arm2.add_vertex((61, 378))
    arm2.add_vertex((55, 380))
    arm2.add_vertex((45, 384))
    arm2.add_vertex((27, 398))
    arm2.add_vertex((24, 397))
    arm2.add_vertex((23, 395))
    arm2.add_vertex((22, 393))
    arm2.add_vertex((38, 381))
    arm2.add_vertex((36, 378))
    arm2.add_vertex((16, 385))
    arm2.add_vertex((9, 383))

    arm2.add_vertex((27, 373))
    arm2.add_vertex((0, 358))
    arm2.add_vertex((43, 355))
    arm2.add_vertex((54, 361))
    arm2.add_vertex((104, 356))
    arm2.add_vertex((155, 355))
    arm2.add_vertex((157, 326))
    arm2.add_vertex((195, 312))
    arm2.add_vertex((198, 315))
    arm2.add_vertex((230, 310))
    arm2.add_vertex((236, 312))
    arm2.add_vertex((268, 310))
    arm2.add_vertex((270, 300))
    arm2.add_vertex((288, 287))
    arm2.add_vertex((326, 276))
    arm2.add_vertex((327, 270))
    arm2.add_vertex((316, 274))
    arm2.add_vertex((330, 258))
    arm2.add_vertex((357, 255))
    arm2.add_vertex((376, 250))
    arm2.add_vertex((395, 257))

    arm2.filled = True
    window.add(arm2)






    face = GPolygon()               #FACE
    face.add_vertex((351, 234))
    face.add_vertex((355, 219))
    face.add_vertex((356, 209))
    face.add_vertex((370, 211))
    face.add_vertex((369, 206))
    face.add_vertex((380, 198))
    face.add_vertex((390, 199))
    face.add_vertex((394, 192))
    face.add_vertex((396, 194))
    face.add_vertex((404, 187))
    face.add_vertex((402, 179))
    face.add_vertex((401, 177))
    face.add_vertex((413, 170))
    face.add_vertex((424, 160))
    face.add_vertex((432, 162))
    face.add_vertex((450, 177))
    face.add_vertex((457, 191))
    face.add_vertex((459, 200))
    face.add_vertex((462, 208))
    face.add_vertex((456, 227))
    face.add_vertex((434, 259))
    face.add_vertex((415, 253))
    face.add_vertex((409, 249))
    face.add_vertex((403, 240))
    face.add_vertex((380, 238))
    face.add_vertex((364, 235))
    face.filled = True
    window.add(face)


    spot1 = GPolygon()
    spot1.add_vertex((353, 199))
    spot1.add_vertex((356, 197))
    spot1.add_vertex((361, 199))
    spot1.add_vertex((369, 196))
    spot1.add_vertex((360, 203))
    spot1.add_vertex((354, 202))
    spot1.filled = True
    window.add(spot1)

    spot2 = GPolygon()
    spot2.add_vertex((357, 220))
    spot2.add_vertex((365, 223))
    spot2.add_vertex((360, 230))
    spot2.add_vertex((354, 229))
    spot2.add_vertex((353, 226))
    spot2.filled = True
    spot2.fill_color = 'white'
    window.add(spot2)

    spot3 = GPolygon()
    spot3.add_vertex((406, 213))
    spot3.add_vertex((408, 220))
    spot3.add_vertex((412, 218))
    spot3.add_vertex((419, 220))
    spot3.add_vertex((413, 217))
    spot3.filled = True
    spot3.fill_color = 'white'
    window.add(spot3)


    face2 = GLine(362, 187,374,179)
    window.add(face2)

    face3 = GLine(374, 179, 388, 163)
    window.add(face3)

    face4 = GLine(388, 163, 397, 159)
    window.add(face4)

    face5 = GLine(397, 159, 406, 160)
    window.add(face5)

    face6 = GLine(406, 160, 424, 160)
    window.add(face6)

    eye = GOval(15,16, x=376, y=173)
    eye.filled = True
    window.add(eye)

    eye2 = GPolygon()
    eye2.add_vertex((385, 175))
    eye2.add_vertex((387, 176))
    eye2.add_vertex((389, 178))
    eye2.add_vertex((387, 183))
    eye2.add_vertex((385, 184))
    eye2.add_vertex((383, 184))
    eye2.add_vertex((381, 183))
    eye2.add_vertex((384, 180))

    eye2.filled = True
    eye2.fill_color = "white"
    window.add(eye2)

    # ears
    ear = GOval(7, 5, x=412, y=203)
    ear.filled = True
    ear.fill_color = "white"
    window.add(ear)

    #RIGHT ARM
    right_arm = GPolygon()
    right_arm.add_vertex((440, 168))
    right_arm.add_vertex((473, 123))
    right_arm.add_vertex((469, 110))
    right_arm.add_vertex((443, 112))
    right_arm.add_vertex((427, 109))
    right_arm.add_vertex((410, 96))
    right_arm.add_vertex((401, 84))
    right_arm.add_vertex((400, 79))
    right_arm.add_vertex((411, 61))
    right_arm.add_vertex((415, 56))
    right_arm.add_vertex((431, 55))
    right_arm.add_vertex((440, 62))
    right_arm.add_vertex((457, 59))
    right_arm.add_vertex((470, 58))
    right_arm.add_vertex((474, 55))
    right_arm.add_vertex((483, 56))
    right_arm.add_vertex((492, 58))
    right_arm.add_vertex((502, 91))
    right_arm.add_vertex((493, 142))
    right_arm.add_vertex((476, 188))
    right_arm.add_vertex((448, 239))
    right_arm.add_vertex((445, 245))
    right_arm.add_vertex((439, 272))
    right_arm.filled = True
    window.add(right_arm)

    #right arm
    right_arm_spot = GPolygon()
    right_arm_spot.add_vertex((440, 168))
    right_arm_spot.add_vertex((473, 123))
    right_arm_spot.add_vertex((463, 150))
    right_arm_spot.add_vertex((476, 149))
    right_arm_spot.add_vertex((465, 180))
    right_arm_spot.add_vertex((458, 196))
    right_arm_spot.add_vertex((453, 183))
    right_arm_spot.filled = True
    right_arm_spot.fill_color = "white"
    window.add(right_arm_spot)

    #ball
    ball = GPolygon()
    ball.add_vertex((404, 40))
    ball.add_vertex((398, 67))
    ball.add_vertex((412, 58))
    ball.add_vertex((433, 54))
    ball.add_vertex((438, 53))
    ball.add_vertex((446, 58))
    ball.add_vertex((448, 60))
    ball.add_vertex((456, 62))
    ball.add_vertex((475, 57))
    ball.add_vertex((479, 56))
    ball.add_vertex((483, 57))
    ball.add_vertex((491, 55))
    ball.add_vertex((494, 46))
    ball.add_vertex((485, 29))
    ball.add_vertex((470, 17))
    ball.add_vertex((405, 42))
    ball.filled = True
    window.add(ball)

    ball2 = GPolygon()
    ball2.add_vertex((407, 40))
    ball2.add_vertex((403, 63))
    ball2.add_vertex((415, 51))
    ball2.add_vertex((430, 51))
    ball2.add_vertex((433, 47))
    ball2.add_vertex((448, 55))
    ball2.add_vertex((449, 54))
    ball2.add_vertex((441, 47))
    ball2.add_vertex((425, 36))
    ball2.add_vertex((422, 31))
    ball2.filled = True
    ball2.fill_color = "white"
    ball2.color = "white"
    window.add(ball2)

    ball3 = GPolygon()
    ball3.add_vertex((424, 23))
    ball3.add_vertex((453, 46))
    ball3.add_vertex((473, 25))
    ball3.add_vertex((455, 13))
    ball3.filled = True
    ball3.fill_color = "white"
    ball3.color = "white"
    window.add(ball3)



    #body
    body1 = GPolygon()
    body1.add_vertex((305, 320))
    body1.add_vertex((309, 342))
    body1.add_vertex((310, 365))
    body1.add_vertex((308, 346))
    body1.add_vertex((301, 331))
    body1.add_vertex((300, 320))
    body1.filled = True
    window.add(body1)

    body2 = GPolygon()
    body2.add_vertex((290, 423))
    body2.add_vertex((294, 447))
    body2.add_vertex((296, 469))
    body2.add_vertex((303, 471))
    body2.add_vertex((310, 481))
    body2.add_vertex((305, 485))
    body2.add_vertex((301, 477))
    body2.add_vertex((295, 474))
    body2.add_vertex((292, 480))
    body2.add_vertex((285, 478))
    body2.add_vertex((290, 470))
    body2.add_vertex((287, 446))
    body2.add_vertex((285, 423))
    body2.filled = True
    window.add(body2)

    body3 = GPolygon()
    body3.add_vertex((283, 593))
    body3.add_vertex((291, 619))
    body3.add_vertex((287, 622))
    body3.add_vertex((280, 596))
    body3.filled = True
    window.add(body3)

    body4 = GPolygon()
    body4.add_vertex((307, 515))
    body4.add_vertex((314, 556))
    body4.add_vertex((324, 592))
    body4.add_vertex((335, 633))
    body4.add_vertex((347, 686))
    body4.add_vertex((339, 633))
    body4.add_vertex((345, 666))
    body4.add_vertex((335, 675))
    body4.add_vertex((315, 610))
    body4.add_vertex((308, 579))
    body4.add_vertex((298, 537))
    body4.add_vertex((300, 514))
    body4.filled = True
    window.add(body4)

    body5 = GPolygon()
    body5.add_vertex((334, 316))
    body5.add_vertex((324, 346))
    body5.add_vertex((315, 273))
    body5.add_vertex((317, 391))
    body5.add_vertex((313, 418))
    body5.add_vertex((316, 453))
    body5.add_vertex((327, 441))
    body5.add_vertex((335, 414))
    body5.add_vertex((346, 386))
    body5.add_vertex((369, 350))
    body5.add_vertex((382, 335))
    body5.add_vertex((354, 323))
    body5.filled = True
    window.add(body5)

    body6 = GPolygon()
    body6.add_vertex((343, 323))
    body6.add_vertex((338, 341))
    body6.add_vertex((325, 355))
    body6.add_vertex((321, 378))
    body6.add_vertex((323, 396))
    body6.add_vertex((319, 439))
    body6.add_vertex((323, 418))
    body6.add_vertex((333, 394))
    body6.add_vertex((341, 374))
    body6.add_vertex((352, 353))
    body6.add_vertex((356, 349))
    body6.add_vertex((373, 334))
    body6.add_vertex((356, 329))
    body6.color = "white"
    body6.filled = True
    body6.fill_color = "white"
    window.add(body6)

    body7 = GPolygon()
    body7.add_vertex((441, 263))
    body7.add_vertex((449, 300))
    body7.add_vertex((443, 302))
    body7.add_vertex((435, 261))
    body7.filled = True
    window.add(body7)

    body8 = GPolygon()
    body8.add_vertex((439, 312))
    body8.add_vertex((438, 343))
    body8.add_vertex((433, 342))
    body8.add_vertex((435, 314))
    body8.filled = True
    window.add(body8)

    body9 = GPolygon()
    body9.add_vertex((430, 308))
    body9.add_vertex((426, 340))
    body9.add_vertex((421, 338))
    body9.add_vertex((425, 309))
    body9.filled = True
    window.add(body9)

    num = GPolygon()
    num.add_vertex((436, 354))
    num.add_vertex((428, 379))
    num.add_vertex((418, 393))
    num.add_vertex((412, 394))
    num.add_vertex((410, 413))
    num.add_vertex((399, 421))
    num.add_vertex((389, 408))
    num.add_vertex((395, 395))
    num.add_vertex((407, 382))
    num.add_vertex((409, 368))
    num.add_vertex((428, 352))
    num.filled = True
    window.add(num)

    num2 = GPolygon()
    num2.add_vertex((421, 368))
    num2.add_vertex((424, 372))
    num2.add_vertex((421, 380))
    num2.add_vertex((416, 382))
    num2.add_vertex((413, 380))
    num2.add_vertex((418, 371))
    num2.filled = True
    num2.fill_color = "white"
    window.add(num2)

    num3 = GPolygon()
    num3.add_vertex((404, 395))
    num3.add_vertex((405, 407))
    num3.add_vertex((396, 410))
    num3.add_vertex((398, 410))
    num3.filled = True
    num3.fill_color = "white"
    window.add(num3)


    #feet
    feet = GPolygon()
    feet.add_vertex((304, 706))
    feet.add_vertex((307, 714))
    feet.add_vertex((305, 728))
    feet.add_vertex((309, 739))
    feet.add_vertex((324, 750))
    feet.add_vertex((340, 754))
    feet.add_vertex((359, 746))
    feet.add_vertex((380, 737))
    feet.add_vertex((395, 759))
    feet.add_vertex((415, 761))
    feet.add_vertex((434, 752))
    feet.add_vertex((440, 745))
    feet.add_vertex((446, 724))
    feet.add_vertex((456, 701))
    feet.add_vertex((489, 667))
    feet.add_vertex((490, 659))
    feet.add_vertex((516, 650))
    feet.add_vertex((521, 654))
    feet.add_vertex((523, 637))
    feet.add_vertex((497, 612))
    feet.add_vertex((487, 627))
    feet.add_vertex((462, 646))
    feet.add_vertex((460, 649))
    feet.add_vertex((454, 643))
    feet.add_vertex((450, 653))
    feet.add_vertex((444, 663))
    feet.add_vertex((430, 657))
    feet.add_vertex((427, 658))
    feet.add_vertex((419, 668))
    feet.add_vertex((408, 675))
    feet.add_vertex((400, 675))
    feet.add_vertex((398, 673))
    feet.add_vertex((359, 691))
    feet.add_vertex((346, 686))
    feet.filled = True
    window.add(feet)

    feet2 = GPolygon()
    feet2.add_vertex((530, 636))
    feet2.add_vertex((542, 640))
    feet2.add_vertex((567, 635))
    feet2.add_vertex((591, 627))
    feet2.add_vertex((594, 630))
    feet2.add_vertex((605, 632))
    feet2.add_vertex((606, 627))
    feet2.add_vertex((598, 625))
    feet2.add_vertex((591, 618))
    feet2.add_vertex((571, 630))
    feet2.add_vertex((542, 635))
    feet2.add_vertex((531, 631))
    feet2.filled = True
    window.add(feet2)

    feet3 = GPolygon()
    feet3.add_vertex((627, 612))
    feet3.add_vertex((625, 603))
    feet3.add_vertex((621, 600))
    feet3.add_vertex((604, 592))
    feet3.add_vertex((524, 569))
    feet3.add_vertex((508, 562))
    feet3.add_vertex((498, 567))
    feet3.add_vertex((513, 574))
    feet3.add_vertex((510, 576))
    feet3.add_vertex((504, 575))
    feet3.add_vertex((506, 586))
    feet3.add_vertex((514, 585))
    feet3.add_vertex((524, 576))
    feet3.add_vertex((547, 588))
    feet3.add_vertex((569, 590))
    feet3.add_vertex((615, 603))
    feet3.filled = True
    window.add(feet3)

    feet4 = GPolygon()
    feet4.add_vertex((630, 601))
    feet4.add_vertex((627, 593))
    feet4.add_vertex((622, 587))
    feet4.add_vertex((611, 580))
    feet4.add_vertex((600, 576))
    feet4.add_vertex((581, 571))
    feet4.add_vertex((579, 575))
    feet4.add_vertex((593, 579))
    feet4.add_vertex((603, 583))
    feet4.add_vertex((612, 588))
    feet4.add_vertex((617, 591))
    feet4.add_vertex((624, 598))
    feet4.add_vertex((627, 604))
    feet4.filled = True
    window.add(feet4)

    feet5 = GPolygon()
    feet5.add_vertex((555, 569))
    feet5.add_vertex((551, 559))
    feet5.add_vertex((545, 555))
    feet5.add_vertex((534, 553))
    feet5.add_vertex((533, 557))
    feet5.add_vertex((543, 561))
    feet5.add_vertex((547, 565))
    feet5.filled = True
    window.add(feet5)

    feet6 = GPolygon()
    feet6.add_vertex((516, 553))
    feet6.add_vertex((505, 555))
    feet6.add_vertex((495, 558))
    feet6.add_vertex((505, 558))
    feet6.add_vertex((515, 557))
    feet6.filled = True
    window.add(feet6)

    feet7 = GPolygon()
    feet7.add_vertex((492, 596))
    feet7.add_vertex((495, 585))
    feet7.add_vertex((493, 606))
    feet7.add_vertex((486, 609))
    feet7.add_vertex((485, 607))
    feet7.add_vertex((490, 602))
    feet7.add_vertex((492, 595))
    feet7.add_vertex((493, 580))
    feet7.filled = True
    window.add(feet7)

    feet8 = GPolygon()
    feet8.add_vertex((656, 538))
    feet8.add_vertex((630, 527))
    feet8.add_vertex((586, 524))
    feet8.add_vertex((583, 536))
    feet8.add_vertex((595, 533))
    feet8.add_vertex((599, 529))
    feet8.add_vertex((606, 534))
    feet8.add_vertex((622, 533))
    feet8.add_vertex((638, 533))
    feet8.add_vertex((653, 542))
    feet8.filled = True
    window.add(feet8)

    feet9 = GPolygon()
    feet9.add_vertex((580, 532))
    feet9.add_vertex((566, 540))
    feet9.add_vertex((545, 534))
    feet9.add_vertex((511, 534))
    feet9.add_vertex((513, 543))
    feet9.add_vertex((509, 544))
    feet9.add_vertex((505, 531))
    feet9.add_vertex((508, 519))
    feet9.add_vertex((512, 513))
    feet9.add_vertex((516, 515))
    feet9.add_vertex((517, 514))
    feet9.add_vertex((513, 527))
    feet9.filled = True
    window.add(feet9)

    feet10 = GOval(8,6, x=528, y=516)
    feet10.filled = True
    window.add(feet10)

    feet11 = GOval(9, 6, x=612, y=544)
    feet11.filled = True
    window.add(feet11)

    feet12 = GOval(4, 9, x=428, y=585)
    feet12.filled = True
    window.add(feet12)

    feet13 = GOval(4, 9, x=429, y=604)
    feet13.filled = True
    window.add(feet13)

    feet14 = GOval(4, 3, x=406, y=651)
    feet14.filled = True
    window.add(feet14)

    feet15 = GOval(4, 3, x=409, y=665)
    feet15.filled = True
    window.add(feet15)

    feet16 = GOval(4, 6, x=415, y=659)
    feet16.filled = True
    window.add(feet16)

    feet17 = GOval(3, 8, x=427, y=652)
    feet17.filled = True
    window.add(feet17)

    feet18 = GOval(3, 8, x=293, y=675)
    feet18.filled = True
    window.add(feet18)

    feet19 = GOval(3, 8, x=305, y=498)
    feet19.filled = True
    window.add(feet19)

    feet20 = GOval(8, 3, x=389, y=447)
    feet20.filled = True
    window.add(feet20)

    feet21 = GOval(25, 3, x=607, y=555)
    feet21.filled = True
    window.add(feet21)

    feet21 = GPolygon()
    feet21.add_vertex((523, 597))
    feet21.add_vertex((533, 616))
    feet21.add_vertex((529, 614))
    feet21.add_vertex((520, 619))
    feet21.filled = True
    window.add(feet21)

    feet22 = GPolygon()
    feet22.add_vertex((648, 524))
    feet22.add_vertex((626, 518))
    feet22.add_vertex((625, 522))
    feet22.add_vertex((643, 526))
    feet22.filled = True
    window.add(feet22)

    feet23 = GPolygon()
    feet23.add_vertex((580, 514))
    feet23.add_vertex((560, 515))
    feet23.add_vertex((560, 517))
    feet23.add_vertex((581, 520))
    feet23.filled = True
    window.add(feet23)

    feet24 = GPolygon()
    feet24.add_vertex((328, 457))
    feet24.add_vertex((395, 602))
    feet24.add_vertex((398, 613))
    feet24.add_vertex((397, 651))
    feet24.add_vertex((385, 611))
    feet24.add_vertex((323, 457))
    feet24.filled = True
    window.add(feet24)

    feet25 = GOval(20, 5, x=318, y=457)
    feet25.filled = True
    window.add(feet25)

    feet26 = GPolygon()
    feet26.add_vertex((331, 675))
    feet26.add_vertex((415, 627))
    feet26.add_vertex((416, 630))
    feet26.add_vertex((397, 654))
    feet26.add_vertex((374, 663))
    feet26.add_vertex((356, 692))
    feet26.add_vertex((348, 692))
    feet26.add_vertex((354, 684))
    feet26.add_vertex((350, 676))
    feet26.filled = True
    window.add(feet26)

    feet27 = GPolygon()
    feet27.add_vertex((291, 505))
    feet27.add_vertex((286, 528))
    feet27.add_vertex((284, 525))
    feet27.add_vertex((282, 540))
    feet27.add_vertex((280, 545))
    feet27.add_vertex((278, 532))
    feet27.add_vertex((282, 519))
    feet27.add_vertex((283, 515))
    feet27.add_vertex((285, 503))

    feet27.filled = True
    window.add(feet27)


if __name__ == '__main__':
    main()

import cozmo
import cozmo.util
from cozmo import faces
from cozmo.faces import Face, EvtFaceRenamed


def cozmo_program(robot: cozmo.robot.Robot):
    while True:
        cozmo.robot.Robot.enable_facial_expression_estimation(robot)
        robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
        f = robot.world.wait_for_observed_face(timeout=10)
        print(f.expression)
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabStaring).wait_for_completed()
        for visible_face in robot.world.visible_faces:
            if visible_face is None:
                print("can't find a face")
            else:
                if f.expression == "happy ":
                    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabVictory).wait_for_completed()

                elif f.expression == "sad":
                    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabSad).wait_for_completed()
                elif f.expression == "angry":
                    robot.play_anim_trigger(cozmo.anim.Triggers.MajorFail).wait_for_completed()
                elif f.expression == "neutral":
                    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabHappy).wait_for_completed()
                elif f.expression == "surprised":
                    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabSurprise).wait_for_completed()
                elif f.expression == "unknown ":
                    print("unknown expression ")

        e = input()

        if e == "exit":
            break


cozmo.run_program(cozmo_program, use_viewer=True)

import unittest
from pid import PID
import time
import random

class PIDTests(unittest.TestCase):

    # def test_stay_zero_when_target_met(self):
    #     pid = PID(0.7,0.1,0.1)
    #     output = pid.update(0, 0)
    #     self.assertEqual(output, 0)
    #
    # def test_stay_zero_when_target_met_over_time(self):
    #     pid = PID(0.7,0.1,0.1)
    #
    #     counter = 0
    #     while (counter != 10):
    #         output = pid.update(0, 0)
    #         self.assertEqual(output, 0)
    #         counter = counter + 1
    #         time.sleep(1)

    def test_return_to_zero_when_target_met(self):
        pid = PID(0.7,0.1,0.1)

        pitch = 100;
        counter = 0;

        while (pitch != 0 and counter != 100):
            output = pid.update(pitch, 0)

            pitch = pitch + output;

            if(pitch < 0):
              pitch = 0


            counter = counter + 1
            time.sleep(1)

        self.assertEqual(pitch, 0)

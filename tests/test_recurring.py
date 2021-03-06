import time

from unittest import TestCase
from unittest.mock import MagicMock

from recurring import job


class TestRecurringTask(TestCase):
    def testGetsCalledRepeatedly(self):
        task = MagicMock()
        r = job(task, 1)
        r.start()
        time.sleep(3)
        r.stop()

        self.assertTrue(1 < task.call_count < 4,
                        "Expected call_count to b 2 or 3, "
                        f"got: {task.call_count}")

    def testChangingRateWorks(self):
        task = MagicMock()
        r = job(task, 1)
        r.start()
        r.rate = 3
        time.sleep(4)
        r.stop()

        self.assertTrue(0 < task.call_count < 3,
                        "Expected call_count to be 1 or 2, "
                        f"got: {task.call_count}")

    def testStartingAfterStopping(self):
        task = MagicMock()
        r = job(task, 1)
        r.start()
        time.sleep(2)
        r.stop()

        first_call_count = task.call_count
        self.assertGreater(first_call_count, 0)

        r.start()
        time.sleep(2)
        r.stop()

        self.assertGreater(task.call_count, first_call_count)

    def testTermination(self):
        task = MagicMock()
        r = job(task, 1)
        r.start()

        time.sleep(2)
        call_count = task.call_count

        r.terminate()

        self.assertEqual(task.call_count, call_count,
                         f'Expected to not have more than {call_count} calls after terminate, got {task.call_count}')

        self.assertFalse(r._scheduler.is_alive(),
                         "Scheduler reports itself as alive after terminate!")

        with self.assertRaisesRegex(RuntimeError, 'Attempt to start terminated job'):
            r.start()

        with self.assertRaisesRegex(RuntimeError, 'Attempt to set the rate of terminated job'):
            r.rate = 4

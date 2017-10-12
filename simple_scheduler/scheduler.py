"""Run the scheduler process."""

from ndscheduler.server import server


class SimpleServer(server.SchedulerServer):

    def post_scheduler_start(self):
        # New user experience! Make sure we have at least 1 job to demo!
        jobs = self.scheduler_manager.get_jobs()
        if len(jobs) == 0:
            self.scheduler_manager.add_job(
                job_class_string='simple_scheduler.jobs.sample_job.Shellob',
                name='List files',
                pub_args=['ls', '-l'],
                minute='*/1')
            self.scheduler_manager.add_job(
                job_class_string='simple_scheduler.jobs.sample_job.Shellob',
                name='Docker check job',
                pub_args=['ps', '-ef | grep python'],
                minute='*/1')


if __name__ == "__main__":
    SimpleServer.run()

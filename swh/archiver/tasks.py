# Copyright (C) 2015-2016  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information

from swh.scheduler.celery_backend.config import app

from .worker import ArchiverWithRetentionPolicyWorker
from .worker import ArchiverToBackendWorker


@app.task(name='swh.archiver.tasks.SWHArchiverWithRetentionPolicyTask',
          bind=True)
def archive_with_retention(self, *args, **kwargs):
    self.log.debug('%s, args=%s, kwargs=%s' % (
        self.name, args, kwargs))
    ArchiverWithRetentionPolicyWorker(*args, **kwargs).run()
    self.log.debug('%s OK' % (self.name))


@app.task(name='swh.archiver.tasks.SWHArchiverToBackendTask',
          bind=True)
def archive_to_backend(self, *args, **kwargs):
    """Main task that archive a batch of content in the cloud.
    """
    self.log.debug('%s, args=%s, kwargs=%s' % (
        self.name, args, kwargs))
    ArchiverToBackendWorker(*args, **kwargs).run()
    self.log.debug('%s OK' % (self.name))

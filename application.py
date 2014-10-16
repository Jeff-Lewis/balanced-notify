#!/usr/bin/env python
from __future__ import unicode_literals
import time
from datetime import datetime

import notify


if __name__ == '__main__':
    while True:
        time.sleep(2)
        print 'doing some work', datetime.utcnow()
    # app = notify.make_app()
    # app.run()

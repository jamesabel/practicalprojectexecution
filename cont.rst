..  _cont:

Continuous Integration
======================

.. image:: _static/continuousintegrationcycle.png

Source : `Agile Test Automation is Incomplete Without Continuous Integration <https://kaizentesting.wordpress.com/2012/08/19/agile-test-automation-is-incomplete-without-continuous-integration/>`_

Continuous delivery is enabled by having automated tests that run in an automated test environment.  Upon every
code check-in to a repository, a test suite is run to ensure the new code does not break existing functionality
(does not 'regress').  Once the test suite passes the new code is allowed to be merged with existing code.

Pull Request Workflow
---------------------

.. image:: _static/pull-request-flow.png

Source: `Pull Request Workflow <https://docs.rhodecode.com/RhodeCode-Enterprise/collaboration/pr-flow.html>`_

Virtually every new feature is developed in its own code branch.  Before starting to work on a new feature (or bug
fix), create a new local branch.  Once your development is complete and you have passed all local tests (you
will most likely want to run the regression test suite), issue a `pull request`.  This may also trigger
a code review.  If the pull request is approved, this branch is merged to the main branch (often called `master`).

Large Files
-----------
Use `GIT Large File Storage <https://git-lfs.github.com/>`_ for large files such as executables.
This is so the repo doesn't grow too large and takes too long to clone.
`Watch this video <https://youtu.be/YQzNfb4IwEY?list=PL7QAN3bnLRocuHOcUZ5Qd2vZ0TOhDE9yp>`_ for
a description of why and how to use git lfs.  As of this writing `git lfs` isn't integrated into PyCharm so if you're
using PyCharm and `git lfs` you'll have to resort to the command line for `git lfs` setup.

Summary
-------

- Use a continuous integration system
- Create branches for new features
- Create and use an automated test suite
- Do pull requests to merge new features to the Master branch

"""
A unit testing fixure for imap_gmail.
"""

import imap_gmail
from test_imap_gmail_login import TEST_IMAP_GMAIL_USERNAME
from test_imap_gmail_login import  TEST_IMAP_GMAIL_PASSWORD





class IMAP_GMAIL_TEST_FIXTURE:

    def __init__(self, fixture_mailbox):
        self.gmail = None
        self.fixture_mailbox = fixture_mailbox


    def __enter__(self):
        self.gmail = imap_gmail.IMAP_GMAIL()
        self.gmail.login(TEST_IMAP_GMAIL_USERNAME, TEST_IMAP_GMAIL_PASSWORD)
        self.gmail.delete(self.fixture_mailbox)
        self.gmail.create(self.fixture_mailbox)

        return self


    def __exit__(self, type, value, traceback):
        self.gmail.logout()

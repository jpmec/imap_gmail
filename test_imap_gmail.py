"""
Tests for imap_gmail.py
"""

import unittest

import imap_gmail

from imap_gmail_unittest_fixture import IMAP_GMAIL_TEST_FIXTURE


class IMAP_GMAIL(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass


    #def test_mailbox_names(self):
    #  result = self.gmail.mailbox_names()
    #
    #  self.assertEqual(result,
    #  [ 'INBOX'
    #  , '[Gmail]'
    #  , '[Gmail]/All Mail'
    #  , '[Gmail]/Drafts'
    #  , '[Gmail]/Important'
    #  , '[Gmail]/Sent Mail'
    #  , '[Gmail]/Spam'
    #  , '[Gmail]/Starred'
    #  , '[Gmail]/Trash'])
    #
    #
    #  result = self.gmail.mailbox_names('[Gmail]')
    #
    #  self.assertEqual(result,
    #  [ '[Gmail]'
    #  , '[Gmail]/All Mail'
    #  , '[Gmail]/Drafts'
    #  , '[Gmail]/Important'
    #  , '[Gmail]/Sent Mail'
    #  , '[Gmail]/Spam'
    #  , '[Gmail]/Starred'
    #  , '[Gmail]/Trash'])
    #
    #
    #def test_messages_count(self):
    #  result = self.gmail.messages_count('INBOX')
    #
    #  self.assertEqual(result, 1)
    #
    #
    #def test_recent_count(self):
    #  result = self.gmail.recent_count('INBOX')
    #
    #  self.assertEqual(result, 0)
    #
    #
    #def test_unseen_count(self):
    #  result = self.gmail.unseen_count('INBOX')
    #
    #  self.assertEqual(result, 0)
    #
    #
    #def test_fetch_header(self):
    #  result = self.gmail.fetch_header('INBOX')
    #
    #  self.assertTrue(result is not None)


    def test_create_folder(self):
        """
        Create a folder
        """

        with IMAP_GMAIL_TEST_FIXTURE('test_create_folder') as fixture:
            status, result = fixture.gmail.delete('my_new_mailbox')

            status, result = fixture.gmail.create('my_new_mailbox')

            self.assertEquals('OK', status)
            self.assertEquals('Success', result[0])

            self.assertEquals('OK', status)
            status, result = fixture.gmail.delete('my_new_mailbox')

            self.assertEquals('Success', result[0])




if __name__ == "__main__":
    unittest.main()

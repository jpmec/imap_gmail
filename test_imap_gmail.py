import unittest
import imaplib, re, time
from email.parser import HeaderParser

import imap_gmail

from test_imap_gmail_login import TEST_IMAP_GMAIL_USERNAME, TEST_IMAP_GMAIL_PASSWORD




class IMAP_GMAIL(unittest.TestCase):

    def setUp(self):
      self.gmail = imap_gmail.IMAP_GMAIL()

      self.gmail.login(TEST_IMAP_GMAIL_USERNAME, TEST_IMAP_GMAIL_PASSWORD)


    def tearDown(self):
      self.gmail.logout()


    def test_mailbox_names(self):
      result = self.gmail.mailbox_names()

      self.assertEqual(result,
      [ 'INBOX'
      , '[Gmail]'
      , '[Gmail]/All Mail'
      , '[Gmail]/Drafts'
      , '[Gmail]/Important'
      , '[Gmail]/Sent Mail'
      , '[Gmail]/Spam'
      , '[Gmail]/Starred'
      , '[Gmail]/Trash'])


      result = self.gmail.mailbox_names('[Gmail]')

      self.assertEqual(result,
      [ '[Gmail]'
      , '[Gmail]/All Mail'
      , '[Gmail]/Drafts'
      , '[Gmail]/Important'
      , '[Gmail]/Sent Mail'
      , '[Gmail]/Spam'
      , '[Gmail]/Starred'
      , '[Gmail]/Trash'])


    def test_messages_count(self):
      result = self.gmail.messages_count('INBOX')

      self.assertEqual(result, 1)


    def test_recent_count(self):
      result = self.gmail.recent_count('INBOX')

      self.assertEqual(result, 0)


    def test_unseen_count(self):
      result = self.gmail.unseen_count('INBOX')

      self.assertEqual(result, 0)


    def test_fetch_header(self):
      result = self.gmail.fetch_header('INBOX')

      self.assertTrue(result is not None)




if __name__ == "__main__":
  unittest.main()

"""
A IMAP interface customized for Gmail.
"""

import imaplib, re
from email.parser import HeaderParser




class IMAP_GMAIL(imaplib.IMAP4_SSL):

    def __init__(self):
        imaplib.IMAP4_SSL.__init__(self, 'imap.gmail.com', port = 993)


    def mailbox_names(self, directory = None, pattern = None):
        """
        Get list of mailbox names.
        """
        re_pattern_str = '^(.+) "(.+)" "(.+)"$'
        re_pattern = re.compile(re_pattern_str)

        if directory is None:
            status, folder_list = self.list()
        else:
            if pattern is None:
                status, folder_list = self.list(directory)
            else:
                status, folder_list = self.list(directory, pattern)

        result = []

        if 'OK' == status:
            for folder in folder_list:
                _, _, mailbox_name = re_pattern.match(folder).groups()
                result.append(mailbox_name)

        return result


    def messages_count(self, mailbox):
        """
        Get integer count of messages for given mailbox.
        """
        status, response = self.status(mailbox, '(MESSAGES)')

        if 'OK' == status:
            re_pattern_str = '^"{0}" \(MESSAGES (\d+)\)$'.format(mailbox)
            re_pattern = re.compile(re_pattern_str)
            re_groups = re_pattern.match(response[0]).groups()

            return int(re_groups[0])
        else:
            return 0


    def recent_count(self, mailbox):
        """
        Get integer count of recent messages for given mailbox.
        """
        status, response = self.status(mailbox, '(RECENT)')

        if 'OK' == status:
            re_pattern_str = '^"{0}" \(RECENT (\d+)\)$'.format(mailbox)
            re_pattern = re.compile(re_pattern_str)
            re_groups = re_pattern.match(response[0]).groups()

            return int(re_groups[0])

        else:
            return 0


    def unseen_count(self, mailbox):
        """
        Get integer count of unseen messages for given mailbox.
        """
        status, response = self.status(mailbox, '(UNSEEN)')

        if 'OK' == status:
            re_pattern_str = '^"{0}" \(UNSEEN (\d+)\)$'.format(mailbox)
            re_pattern = re.compile(re_pattern_str)
            re_groups = re_pattern.match(response[0]).groups()

            return int(re_groups[0])

        else:
            return 0


    def fetch_header(self, mailbox):
        """
        Get a mailbox header.
        """

        self.select(mailbox)
        status, fetch_data = self.fetch('1', '(BODY.PEEK[HEADER])')
        self.close()

        header_parser = HeaderParser()
        header = header_parser.parsestr(fetch_data[0][1])

        if status == 'OK':
            return header
        else:
            return None


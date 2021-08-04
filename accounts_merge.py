from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        # check if the list is empty
        if not accounts: return [[]]
        if not accounts[0]: return [[]]

        # hash all contacts by each email
        # insert to hash only if all emails are not in keys
        # otherwise, merge by key
        emails_hash = {}

        for account in accounts:
            name = account[0]
            emails = account[1:]

            not_exists = True
            for email in emails:
                if email in emails_hash:
                    not_exists = False
                    existing_account = emails_hash[email]
                    existing_name = existing_account[0]
                    existing_emails = existing_account[1:]
                    merged_mails = sorted(list(set(emails + existing_emails)))
                    existing_account.clear()
                    existing_account.append(existing_name)
                    existing_account.extend(merged_mails)
                    account = existing_account
            if not_exists:
                name = account[0]
                emails = account[1:]
                new_account = [name] + sorted(emails)
                for email_2 in emails:
                    emails_hash[email_2] = new_account

        # return hash values
        unique_acc = list(set(map(lambda x: tuple(x), emails_hash.values())))
        unique_acc.sort(key=lambda x: x[0])
        unique_acc = list(map(lambda x: list(x), unique_acc))
        return unique_acc


if __name__ == '__main__':
    ans = Solution().accountsMerge(
        [["David", "David0@m.co", "David4@m.co", "David3@m.co"], ["David", "David5@m.co", "David5@m.co", "David0@m.co"],
         ["David", "David1@m.co", "David4@m.co", "David0@m.co"], ["David", "David0@m.co", "David1@m.co", "David3@m.co"],
         ["David", "David4@m.co", "David1@m.co", "David3@m.co"]]
    )

    print(ans)

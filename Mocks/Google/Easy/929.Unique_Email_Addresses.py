class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_emails = set()
        
        for email in emails:
            [local_name,domain_name] = email.split('@')
            local_name_parts = local_name.split('+')
            local_name_final = local_name_parts[0].replace('.','')
            
            unique_emails.add(local_name_final+'@'+domain_name)
        
        #print unique_emails
        return len(unique_emails)

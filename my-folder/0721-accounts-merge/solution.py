class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        email_to_name = {}

        for acc in accounts:
            user_name = acc[0]
            first_email = acc[1]
            for email in acc[1:]:
                graph[first_email].append(email)
                graph[email].append(first_email)
                email_to_name[email] = user_name

        def dfs(email, visited, emails):
            stack = [email]
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    emails.append(node)
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            stack.append(neighbor)

        visited = set()
        merged_accounts = []

        for email in graph:
            if email not in visited:
                emails = []
                dfs(email, visited, emails)
                merged_accounts.append([email_to_name[email]] + sorted(emails))

        return merged_accounts

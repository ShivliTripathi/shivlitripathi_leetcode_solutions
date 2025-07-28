class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        pattern = r'^(?!.*(.)\1).+$'
        special_char = r'[!@#$%^&*()\-\+]'
        return (len(password) >=8 and any(p.islower() for p in password) and 
        any(p.isupper() for p in password) and bool(re.search(special_char, password)) and any(p.isdigit() for p in password) and bool(re.match(pattern, password)))
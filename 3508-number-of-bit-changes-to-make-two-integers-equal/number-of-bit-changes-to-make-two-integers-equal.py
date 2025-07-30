class Solution:
    def minChanges(self, n: int, k: int) -> int:
        bin_n= bin(n)[2:]
        bin_k= bin(k)[2:]

        if len(bin_n)>len(bin_k):
            l=len(bin_n)-len(bin_k)
            while l>0:
                bin_k = '0'+ bin_k
                l-=1
        else:
            l=len(bin_k)-len(bin_n)
            while l>0:
                bin_n = '0'+ bin_n
                l-=1

        cnt=0
        bin_n_list = list(bin_n)
        bin_k_list = list(bin_k)

        for i in range(len(bin_n_list)):
            if bin_n_list[i]==bin_k_list[i]:
                continue
            elif bin_k_list[i] != bin_n_list[i] and bin_k_list[i]=='0':
                bin_k_list[i]=bin_n_list[i]
                cnt+=1
        
        bin_n = ''.join(bin_n_list)
        bin_k = ''.join(bin_k_list)

        if bin_n == bin_k:
            return cnt
        else:
            return -1
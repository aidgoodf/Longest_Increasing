#!/usr/bin/env python
# coding: utf-8

# 
# ## Aidan Goodfellow

# In[25]:


def LIS(A):
    n = len(A)
    
    # lengths[i] will store the length of the LIS ending at index i
    lengths = [1] * n
    
    # prev[i] will store the index of the previous element in the LIS ending at index i
    prev = [-1] * n
    
    # Find the length of the LIS for each element
    for i in range(1, n):
        for j in range(i):
            if A[i] > A[j] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                prev[i] = j
    
    # Find the index of the maximum length
    max_index = lengths.index(max(lengths))
    
    # Reconstruct the LIS
    B = []
    while max_index != -1:
        B.append(A[max_index])
        max_index = prev[max_index]
    
    B = B[::-1]  # Reverse to get the correct order
    print("Length of LIS:", len(B))
    return B


# In[26]:


def INC_DEC(A):
    n = len(A)
    
    # inc[i] stores the length of the longest increasing subsequence ending at i
    # dec[i] stores the length of the longest decreasing subsequence starting from i
    inc = [1] * n
    dec = [1] * n
    
    prev_inc = [-1] * n
    prev_dec = [-1] * n
    
    # Compute inc[] values
    for i in range(1, n):
        for j in range(i):
            if A[i] > A[j] and inc[i] < inc[j] + 1:
                inc[i] = inc[j] + 1
                prev_inc[i] = j
                
    # Compute dec[] values
    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if A[i] > A[j] and dec[i] < dec[j] + 1:
                dec[i] = dec[j] + 1
                prev_dec[i] = j
                
    # Find the end index of the inc/dec subsequence
    end_idx = 0
    max_len = inc[0] + dec[0] - 1
    for i in range(n):
        if inc[i] + dec[i] - 1 > max_len:
            max_len = inc[i] + dec[i] - 1
            end_idx = i
            
    # Reconstruct the inc/dec subsequence
    incdec_seq = []
    
    # First, the increasing part
    idx = end_idx
    while idx != -1:
        incdec_seq.append(A[idx])
        idx = prev_inc[idx]
    
    # Reverse to get the correct order for the increasing part
    incdec_seq = incdec_seq[::-1]
    
    # Then, the decreasing part (excluding the peak element as it's already included)
    idx = prev_dec[end_idx]
    while idx != -1:
        incdec_seq.append(A[idx])
        idx = prev_dec[idx]
    
    print("Length of Longest inc/dec Subsequence:", max_len)
    return incdec_seq


# In[27]:


import ipytest
ipytest.autoconfig()


# In[28]:


get_ipython().run_cell_magic('ipytest', '', '\n# test cases for py.test\ndef testLis():\n    assert LIS([1, 5, 6]) == [1, 5, 6]\n    assert LIS([1, 5, 6, 4]) == [1, 5, 6]\n    assert LIS([1, 5, 6, 2, 3, 4, 7]) == [1, 2, 3, 4, 7]\n    assert LIS([1, 5, 2, 6, 3, 7, 4, 9, 8, 10]) == [1, 5, 6, 7, 9, 10]\n    assert LIS([0, 4, 2, 8, 22, 12, 3, 6, 5]) == [0, 4, 8, 22]\n\ndef testIncDec():\n    assert INC_DEC([1, 5, 3]) == [1, 5, 3]\n    assert INC_DEC([1, 5, 6, 4]) == [1, 5, 6, 4]\n    assert INC_DEC([1, 5, 6, 3, 9, 4, 10, 2]) == [1, 5, 6, 9, 4, 2]\n    assert INC_DEC([1, 100, 200, 300, 80, 77, 70, 40, 30 , 120, 400, 500, 600, 700, 405, 800, 5, 4]) == [1, 100, 200, 300, 80, 77, 70, 40, 30, 5, 4]')


# In[ ]:





# In[ ]:





# In[ ]:





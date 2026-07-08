#MERGE STORTED array
def merge(nums1, nums2):
    return sorted(nums1 + nums2)


nums1 = [1,2,3]
nums2 = [2,4,6]

print(merge(nums1, nums2))
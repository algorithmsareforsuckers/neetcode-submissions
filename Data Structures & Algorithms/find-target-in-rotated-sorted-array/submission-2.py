class Solution:
    def search(self, nums: List[int], target: int) -> int:
        zero = nums[0]
        ma = 0

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r-l)//2
            print(mid, nums[mid])
            if nums[mid] == target:
                return mid #early stopping

            if nums[mid] < zero:
                # index is >= rotation number
                r = mid - 1
            
            else:
                if nums[mid] >= nums[ma]:
                    ma = mid
                l = mid + 1
        print(ma)
        
        # ma is the index of the largest element in array.
        if zero <= target <= nums[ma]:
            l = 0
            r = ma
            while l <= r:
                mid = l + (r-l)//2
                print(mid, nums[mid])
                if nums[mid]==target:
                    return mid
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        l = ma
        r = len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

        
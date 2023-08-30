class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        root = TreeNode(nums[n//2])
        ans = root
        sma = nums[:n//2]
        lar = nums[n//2+1:]
        def builder(root,sma,lar):
            if len(sma)==0 and len(lar)==0:
                return
            
            sma_h = len(sma)//2
            lar_h = len(lar)//2
            if sma:
                root.left = TreeNode(sma[sma_h])
                builder(root.left,sma[:sma_h],sma[sma_h+1:]) 
            if lar:
                root.right = TreeNode(lar[lar_h])
                builder(root.right,lar[:lar_h],lar[lar_h+1:]) 
        
        builder(root,sma,lar)
        return ans
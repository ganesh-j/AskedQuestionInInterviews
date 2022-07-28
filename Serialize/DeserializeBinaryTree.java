/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {
    static int index = 0;
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        
         //do the preorder traversal
        ArrayList<String> res = new ArrayList<String>();
        preOrderTraversal(root, res);
        String temp =  String.join(",", res);
        System.out.println("output string is"+temp);
        return temp;
    }
    
    
    public void preOrderTraversal(TreeNode root, ArrayList<String> res) {
        
        if (root == null) {
            res.add("-1");
            return;
        }
        res.add(String.valueOf(root.val));
        preOrderTraversal(root.left, res);
        preOrderTraversal(root.right, res);
        
    }
        
    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        
          String[] res = data.split(",");
          return helper(res);
        
    }
    public TreeNode helper(String[] res) {
        ****// v.imp: do not use == for string comparison
            //use .equals to for string comparison
          if (index >= res.length || res[index].equals("-1")) {
              return null;
          }
      
          TreeNode node = new TreeNode(Integer.parseInt(res[index]));
          index++;
          node.left = helper(res);
          
          index++;
          node.right = helper(res);
        
          return node;
          
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));
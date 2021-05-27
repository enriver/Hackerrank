class Node{
    int val;	//Value
    int ht;		//Height
    Node left;	//Left child
    Node right;	//Right child

    Node(){
        
    }

    Node(int val, int ht, Node left, Node right){
        this.val=val;
        this.ht=ht;
        this.left=left;
        this.right=right;
    }

    static Node insert(Node root,int val)
    {
    	if(root==null){
            root=new Node();
            root.val=val;
            root.ht=setHeight(root);
            return root;
        }
        if(val <= root.val){ // if inputed value is less than root.val
            root.left=insert(root.left, val);
        }
        else if(val > root.val){ // if inputed value is bigger than root.val
            root.right=insert(root.right,val);
        }
        
        int balanceFactor=height(root.left)-height(root.right);
        
        if(balanceFactor>1){
            if(height(root.left.left)>=height(root.left.right))
                root=rightRotate(root);
            else{
                root.left=leftRotate(root.left);
                root=rightRotate(root);
            }
        }else if(balanceFactor<-1){
            if(height(root.right.right)>=height(root.right.left))
                root=leftRotate(root);
            else{
                root.right=rightRotate(root.right);
                root=leftRotate(root);
            }
        }else{
            root.ht=setHeight(root);
        }
        return root;
    }
    static Node rightRotate(Node root){
        Node newRoot=root.left;
        root.left=newRoot.right;
        newRoot.right=root;
        root.ht=setHeight(root);
        newRoot.ht=setHeight(newRoot);
        return newRoot;
    }
    static Node leftRotate(Node root){
        Node newRoot=root.right;
        root.right=newRoot.left;
        newRoot.left=root;
        root.ht=setHeight(root);
        newRoot.ht=setHeight(newRoot);
        return newRoot;
    }
    static int height(Node root){
        if(root==null) return -1;
        else return root.ht;
    }
    static int setHeight(Node root){
        if(root==null) return -1;
        else return 1+Math.max(height(root.left), height(root.right));
    }
}
    	


	
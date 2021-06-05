package Graph;

public class GraphMain {
    public static void main(String[] args){
        Graph g=new IncMatrix(7,12);
        g.addEdge(0,1,2);
        g.addEdge(0,3,1);
        g.addEdge(1,3,3);
        g.addEdge(1,4,10);
        g.addEdge(2,0,4);
        g.addEdge(2,5,5);
        g.addEdge(3,2,2);
        g.addEdge(3,4,2);
        g.addEdge(3,5,8);
        g.addEdge(3,6,4);
        g.addEdge(4,6,6);
        g.addEdge(6,5,1);

        System.out.println(g.toString());
    }
}

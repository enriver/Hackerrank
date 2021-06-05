package Graph;

public class Edge implements Comparable<Edge>{
    private int u,v;
    private double weight;

    Edge n;

    public Edge(int x, int y, double w, Edge next){
        this.u=x;
        this.v=y;
        this.weight=x;
        this.n=next;
    }
    public int getTail(){
        return u;
    }
    public int getHead(){
        return v;
    }
    public double getWeight(){
        return weight;
    }
    public int compareTo(Edge e){
        if(weight<e.weight) return -1;
        else if(weight>e.weight) return 1;
        else return 0;
    }
    public String toString(){
        return "("+u+","+v+"):"+weight;
    }
}

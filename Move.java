
public class Move {
	
    private Player player;
    private Spot start;
    private Spot end;
    private Piece pieceMoved;
    //not sure if I need this
    private boolean passBall = false;
  
    public Move(Player player, Spot start, Spot end){
    	
        this.player = player;
        this.start = start;
        this.end = end;
        this.pieceMoved = start.getPiece();
        
    }
  
    public boolean didPassBall(){
    	
        return this.passBall;
    }
  
    public void setPassBall(boolean passBall){
    	
        this.passBall = passBall;
    }
    
    public Spot getStart() {
    	return this.start;
    }
    
    public Spot getEnd() {
    	return this.end;
    }
    
}
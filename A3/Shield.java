import java.util.ArrayList;

public class Shield extends BoardComponent implements IObserver  {

    private int shieldHealth;
     BoardComponent shielded;
    private int x,y;
    
    // shield component 
    public Shield(BoardComponent bc, int x, int y)
    {
        super();
        shielded = bc;
        shieldHealth = 2;
        this.x = x;
        this.y = y;
    }

    @Override
    public void Operation() {

    }

    // shield add operation
    @Override
    public void Add(BoardComponent child) {
        shielded.Add(child);
    }

    // shield remove operation
    @Override
    public void Remove(BoardComponent child) {
        shielded.Remove(child);
    }

    // update operation
    @Override
    public void Update() {
	    shieldHealth = shieldHealth -1;
	    if (shieldHealth == 0)
	    {ArrayList<ArrayList<BoardComponent>> board = GameBoard.Instance().GetBoard();
	     board.get(x).set(y,shielded);}
        }
}

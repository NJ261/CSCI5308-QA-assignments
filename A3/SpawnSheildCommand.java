import java.util.ArrayList;

public class SpawnSheildCommand extends Command {

    public SpawnSheildCommand(Object receiver,String[]args)
    {
        super(receiver,args);
    }

    @Override
    public void Execute() {

        IAsteroidGameFactory factory = GameBoard.Instance().GetFactory();
        
        // x and y axis parsing
        int x = Integer.parseInt(args[0]);
        int y = Integer.parseInt(args[1]);
        
        ArrayList<ArrayList<BoardComponent>> board = GameBoard.Instance().GetBoard();
        Square currentSquare = (Square) receiver;
        
        // shield decorator
        BoardComponent decorator = new Shield(currentSquare,x,y);
        board.get(x).set(y,decorator);
        
        // shield spawning
        System.out.println("Spawning sheild at (" + args[0] + "," + args[1] + ")");
    }
}
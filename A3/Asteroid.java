// Asteroid is a leaf component in the composite structure
public class Asteroid extends BoardComponent
{
	private int height;
	
	public Asteroid(int height)
	{
		super();
		this.height = height;
	}
	
	@Override
	public void Operation()
	{
		height -= 1;
		if (0 == height)
		{
			parent.Remove(this);		
		}
	}

	@Override
	public void Add(BoardComponent child)
	{
		// I'm a leaf!
	}

	@Override
	public void Remove(BoardComponent child)
	{
		// I'm a leaf!
	}	
}

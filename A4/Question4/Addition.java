public class Addition extends MathOperation {
	private int leftOperand;
	private int rightOperand;
	
	public Addition(int leftOperand, int rightOperand) {
        super(leftOperand, rightOperand);
        this.leftOperand=leftOperand;
        this.rightOperand=rightOperand;
    }

    public int GetResult() {
        return leftOperand + rightOperand;
    }
}




import javax.swing.*;
import java.awt.*;
import java.util.*;
import java.util.concurrent.TimeUnit;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

// A game of Minesweeper, written in Java. Hold down the shift key when
// you click the squares to flag them. If a square says "no" after you click
// it, that means there are no mines around it. Enjoy!

public class JavaSweeper extends JFrame {
	public static void main(String[] args) {
		new JavaSweeper();
	}
	
	private static void sleepMillis(int millis) {
		try {
			TimeUnit.MILLISECONDS.sleep(millis);
		} catch (InterruptedException ie) {
			ie.printStackTrace();
		}
	}
	public JavaSweeper() {
		setBounds(550, 200, 315, 340);
		setVisible(true);
		setTitle("JavaSweeper");
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		Container c = this.getContentPane();
		Button sacrificialbtn = new Button();
		Button [] btn = new Button[100];
		int[] random = new int[100];
		for (int x = 0; x < 100; x++) {
			random[x] = -1;
		}
		for (int x = 0; x < 15; x++) {
			int ranNum =(int) (Math.random()*100);
			if (random[ranNum] != ranNum) {
				random[ranNum] = ranNum;
			} else {
				x--;
			}
		}
		for (int x = 0; x < 100; x++) {
			btn[x] = new Button();
			btn[x].setBackground(Color.lightGray);
			btn[x].setVisible(true);
			setListener(btn, random, x);
			sleepMillis(5);
		}
		int runThrough = 0;
		for (int x = 0; x < 10; x++) {
			for (int y = 0; y < 10; y++) {
				btn[runThrough].setBounds(x*30, y*30, 30, 30);
				runThrough++;
			}
		}
		sacrificialbtn.setVisible(false);
		for (int x = 0; x < 100; x++) {
			c.add(btn[x]);
		}
		c.add(sacrificialbtn);
		doLayout();
		validate();
	}
	public void setListener (Button[] butn, int[] randoms, int run) {
		butn[run].addMouseListener(new MouseListener () {
			int x = -1;
			boolean clickedOn = false;
			@Override
			public void mouseClicked(MouseEvent e) {
				boolean runner = false;
				int mineNum = 0;
				for (int y = 0; y < 100; y++) {
					if (run == randoms[y]) {
						runner = true;
					}
				}
				//checks one square up for mines
				if (!runner && run != 0 && run != 10 && run != 20 && run != 30 && run != 40 && run != 50 && run != 60 && run != 70 && run != 80 && run != 90) {
					for (int y = 0; y < 100; y++) {
						int lookForMine = run - 1;
						if (lookForMine == randoms[y]) {
							mineNum++;
						}
					}
				}
				//checks one square down for mines
				if (!runner && run != 9 && run != 19 && run != 29 && run != 39 && run != 49 && run != 59 && run != 69 && run != 79 && run != 89 && run != 99) {
					for (int y = 0; y < 100; y++) {
						int lookForMine = run + 1;
						if (lookForMine == randoms[y]) {
							mineNum++;
						}
					}
				}
				//checks one square to the left for mines
				if (!runner && run != 0 && run != 1 && run != 2 && run != 3 && run != 4 && run != 5 && run != 6 && run != 7 && run != 8 && run != 9) {
					for (int y = 0; y < 100; y++) {
						int lookForMine = run - 10;
						if (lookForMine == randoms[y]) {
							mineNum++;
						}
					}
				}
				//checks one square to the right for mines
				if (!runner && run != 90 && run != 91 && run != 92 && run != 93 && run != 94 && run != 95 && run != 96 && run != 97 && run != 98 && run != 99) {
					for (int y = 0; y < 100; y++) {
						int lookForMine = run + 10;
						if (lookForMine == randoms[y]) {
							mineNum++;
						}
					}
				}
				//checks one square up and to the left for mines
				if (!runner && run != 0 && run != 1 && run != 2 && run != 3 && run != 4 && run != 5 && run != 6 && run != 7 && run != 8 && run != 9 && run != 10 && run != 20 && run != 30 && run != 40 && run != 50 && run != 60 && run != 70 && run != 80 && run != 90) {
					for (int y = 0; y < 100; y++) {
						int lookForMine = run - 11;
						if (lookForMine == randoms[y]) {
							mineNum++;
						}
					}
				}
				//checks one square up and to the right for mines
				if (!runner && run != 90 && run != 91 && run != 92 && run != 93 && run != 94 && run != 95 && run != 96 && run != 97 && run != 98 && run != 99 && run != 0 && run != 10 && run != 20 && run != 30 && run != 40 && run != 50 && run != 60 && run != 70 && run != 80) {
					for (int y = 0; y < 100; y++) {
						int lookForMine = run + 9;
						if (lookForMine == randoms[y]) {
							mineNum++;
						}
					}
				}
				//checks one square down and to the left for mines
				if (!runner && run != 0 && run != 1 && run != 2 && run != 3 && run != 4 && run != 5 && run != 6 && run != 7 && run != 8 && run != 9 && run != 19 && run != 29 && run != 39 && run != 49 && run != 59 && run != 69 && run != 79 && run != 89 && run != 99) {
					for (int y = 0; y < 100; y++) {
						int lookForMine = run - 9;
						if (lookForMine == randoms[y]) {
							mineNum++;
						}
					}
				}
				//checks one square down and to the right for mines
				if (!runner && run != 90 && run != 91 && run != 92 && run != 93 && run != 94 && run != 95 && run != 96 && run != 97 && run != 98 && run != 99 && run != 9 && run != 19 && run != 29 && run != 39 && run != 49 && run != 59 && run != 69 && run != 79 && run != 89) {
					for (int y = 0; y < 100; y++) {
						int lookForMine = run + 11;
						if (lookForMine == randoms[y]) {
							mineNum++;
						}
					}
				}
				if (e.isShiftDown()) {
					if (x == -1) {
						butn[run].setBackground(Color.pink);
						x *= -1;
						//checks if all the bombs are marked
						boolean falseStart = false;
						int check15 = 0;
						for (int y = 0; y < 100; y++) {
							if (y != randoms[y] && butn[y].getBackground() == Color.pink) {
								falseStart = true;
							} else {
								if  (y == randoms[y] && butn[y].getBackground() == Color.pink) { 
									check15++;
								}
							}
						}
						if (check15 == 15 && !falseStart) {
							JOptionPane.showMessageDialog(null, "Yay! You found all the mines! Once you close this pane, these windows will close.", "You Won!", JOptionPane.PLAIN_MESSAGE);
							System.exit(0);
						}
					} else {
						if (!clickedOn) {
							butn[run].setBackground(Color.lightGray);
						} else {
							butn[run].setBackground(Color.gray);
						}
						x *= -1;
						//checks if all the bombs are marked
						boolean falseStart = false;
						int check15 = 0;
						for (int y = 0; y < 100; y++) {
							if (y != randoms[y] && butn[y].getBackground() == Color.pink) {
								falseStart = true;
							} else {
								if  (y == randoms[y] && butn[y].getBackground() == Color.pink) { 
									check15++;
								}
							}
						}
						if (check15 == 15 && !falseStart) {
							JOptionPane.showMessageDialog(null, "Yay! You found all the mines! Once you close this pane, these windows will close.", "You Won!", JOptionPane.PLAIN_MESSAGE);
							System.exit(0);
						}
					}
				} else {
					clickedOn = true;
					if (runner) {
						butn[run].setBackground(Color.red);
						for (int y = 0; y < 100; y++) {
							if (randoms[y] != -1 && randoms[y] != run) {
								butn[y].setBackground(Color.red);
							}
						}
						JOptionPane.showMessageDialog(null, "Oh no! You hit a mine! The windows will close when you close this one.");
						System.exit(0);
					} else {
						if (mineNum == 0) {
							butn[run].setBackground(Color.gray);
							butn[run].setLabel("no");
						} else {
							butn[run].setBackground(Color.gray);
							if (mineNum == 1) {
								butn[run].setForeground(Color.blue);
							}
							if (mineNum == 2) {
								butn[run].setForeground(Color.red);
							}
							if (mineNum == 3) {
								butn[run].setForeground(Color.magenta);
							}
							if (mineNum == 4) {
								butn[run].setForeground(Color.orange);
							}
							if (mineNum == 5) {
								butn[run].setForeground(Color.cyan);
							}
							if (mineNum == 6) {
								butn[run].setForeground(Color.black);
							}
							if (mineNum == 7) {
								butn[run].setForeground(Color.green);
							}
							if (mineNum == 8) {
								butn[run].setForeground(Color.yellow);
							}
							butn[run].setLabel(new Integer(mineNum).toString());
						}
					}
				}
			}
			@Override
			public void mouseEntered(MouseEvent e) {
			}
			@Override
			public void mouseExited(MouseEvent e) {
			}
			@Override
			public void mousePressed(MouseEvent e) {
			}
			@Override
			public void mouseReleased(MouseEvent e) {
			}		
			}
		);
	}
}

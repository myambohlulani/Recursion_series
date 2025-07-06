import javax.swing.JFrame;
import java.awt.Color;
import javax.swing.ImageIcon;

public class BeginnerFrame extends JFrame {
    BeginnerFrame() {
        // setting title.
        this.setTitle("Hello, World!");
        // setting the size of the windows.
        this.setSize(800, 500);
        // turning of the resizeable.
        this.setResizable(false);
        // closing the windows instead of hiding it.
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // setting the icon
        ImageIcon image = new ImageIcon("code.png");
        this.setIconImage(image.getImage());

        // changing the background color
        this.getContentPane().setBackground(new Color(20, 69, 40));

        // making the windows visible
        this.setVisible(true);
    }
}
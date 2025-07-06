package GUI;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import java.awt.Color;

public class MyFrame extends JFrame {
    // CONSTRUCTOR
    MyFrame() {
        // JFrame frame = new JFrame(); // creating a frame but not visible
        // setting the title of frame
        this.setTitle("Hlulani GUI title");

        // exit out of Application
        // Default one is HIDE_ON_CLOSE, There is DO_NOTHING_ON_CLOSE too
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // prevent frame from being resized
        this.setResizable(false);

        // setting the size of the frame
        this.setSize(420, 420); // width and height

        // making the frame visible, this comes at the end.
        this.setVisible(true);

        // setting image
        ImageIcon image = new ImageIcon("code.png");
        this.setIconImage(image.getImage()); // changing icon of frame

        // changing the background color using rgb
        this.getContentPane().setBackground(new Color(55, 155, 100));
    }
}

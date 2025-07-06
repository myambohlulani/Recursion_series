package GUI;

// import java.awt.Color;
// import javax.swing.ImageIcon;
// import javax.swing.JFrame;

public class Main {
    // JFrame => Gui window to add componenets to

    public static void main(String[] args) {
        // JFrame frame = new JFrame(); // creating a frame but not visible

        // // setting the title of frame
        // frame.setTitle("Hlulani GUI title");

        // // exit out of Application
        // // Default one is HIDE_ON_CLOSE, There is DO_NOTHING_ON_CLOSE too
        // frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // // prevent frame from being resized
        // frame.setResizable(false);

        // // setting the size of the frame
        // frame.setSize(420, 420); // width and height

        // // making the frame visible, this comes at the end.
        // frame.setVisible(true);

        // // setting image
        // ImageIcon image = new ImageIcon("code.png");
        // frame.setIconImage(image.getImage()); // changing icon of frame

        // // changing the background color using rgb
        // frame.getContentPane().setBackground(new Color(55, 155, 100));
        // MyFrame myFrame = new MyFrame();

        new MyFrame();
    }
}

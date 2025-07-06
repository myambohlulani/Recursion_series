package GUI;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.border.Border;
import javax.swing.BorderFactory;

import java.awt.Color;
import java.awt.Font;

import javax.swing.ImageIcon;

public class Labelss {
    // JLabel => A gui display area for a string of text, an image or both
    public static void main(String[] args) {
        // creating a label
        JLabel label = new JLabel();
        Border border = BorderFactory.createLineBorder(Color.GREEN, 4);
        // setting texts for the label
        label.setText("Hlulani Myambo is coding."); // setting text of label

        // creating an image
        ImageIcon icon = new ImageIcon("code.png");
        label.setIcon(icon);

        // Frame
        JFrame frame = new JFrame();
        frame.setTitle("Labels Exercise");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 500);
        // frame.setResizable(false);
        /*
         * Images are inserted on the left side of texts by default and the texts are
         * placed on the right.
         */

        // moving the texts
        label.setHorizontalTextPosition(JLabel.CENTER); // THIS WILL OVERLAP
        // LEFT, CENTER, RIGHT of the image icon
        label.setVerticalTextPosition(JLabel.CENTER); // TOP, CENTER, BOTTOM relative to the icon

        // changing the color
        label.setForeground(new Color(155, 100, 155));

        // setting the font style and width
        label.setFont(new Font("MV Boli", Font.PLAIN, 40));

        // displacing the image and the label
        label.setIconTextGap(100);// -ve for close and +ve for far away

        // changing the background color
        label.setBackground(Color.BLACK);
        label.setOpaque(true); // display background color

        // border
        label.setBorder(border);

        // displaying the label
        frame.add(label);
        frame.setVisible(true);
    }
}

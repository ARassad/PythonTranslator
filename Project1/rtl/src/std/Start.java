/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package std;

import java.util.HashMap;

/**
 *
 * @author Arkadi
 */
public class Start {
    public static void main(String[] args) throws Exception {
        System.out.println("Create program class.");
        MainClass program = new MainClass();
        
        System.out.println("Main function start.");
        program.__call__();
        System.out.println("Main function end.");
        
        System.out.println("Program local variable : ");
        for(HashMap.Entry<String, __PyGenericObject> entry : program.__dir__.entrySet()) {
            String key = entry.getKey();
            __PyGenericObject value = entry.getValue();
            System.out.println("Key : " + key + ", Value : " + value.__str__().__string__);
        }
    }
}

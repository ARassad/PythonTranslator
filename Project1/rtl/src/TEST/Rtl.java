/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package TEST;
import std.__PyInteger;
import std.__PyFloat;
import std.__PyGenericObject;
import std.__PyMethod;
import std.__PyObject;
import std.__PyString;
/**
 *
 * @author 1
 */
public class Rtl {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws Exception {
        // TODO code application logic here
        __PyObject foo = new __PyMethod();
        __PyGenericObject INT = new __PyInteger(123);
        foo.__setattr__("INT", INT);
        
        foo.__dir__.putAll(foo.__dir__);
        
        foo.__call__();
    }
    
}

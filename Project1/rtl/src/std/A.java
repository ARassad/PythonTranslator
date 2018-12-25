/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package std;

/**
 *
 * @author Arkadi
 */
public class A extends __PyGenericObject{
    public __PyGenericObject __call__(__PyGenericObject a, __PyGenericObject b) throws Exception{
        this.__setattr__("i", new __PyInteger(145678));
        this.__setattr__("f", new __PyFloat((float)12415151.134234));
        this.__setattr__("s", new __PyString("strVal"));
        return this.__getattr__("s").__abs__();
    }
}

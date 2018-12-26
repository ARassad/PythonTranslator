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
        this.__setattr__("a", a);
        this.__setattr__("b", b);
        return null;
    }
}

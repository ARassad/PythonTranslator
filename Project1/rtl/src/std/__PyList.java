/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package std;

import java.util.LinkedList;
import sun.reflect.generics.reflectiveObjects.NotImplementedException;

/**
 *
 * @author Arkadi
 */
public class __PyList extends __PyObject {

    public __PyList() {
        super();
        __list__ = new LinkedList<>();
    }
    
    //Type cast
    public __PyObject __str__() throws Exception{
        String res = "[";
        int l = __list__.size();
        for(int i = 0; i < l; i++){
            res = res + this.__list__.get(i).__str__();
            if(i != l - 1)
                res = res + ',';
        }
        res = res + ']';
        return new __PyString(res);
    }
    
    public __PyObject __list__(){
       return this;
    }
    
    public __PyObject __bool__() {
       return new __PyInteger(this.__list__.size() != 0);
    }
    
    // List 
    public __PyObject __contains__(__PyObject value) {
        boolean found = false;
        int l = this.__list__.size();
        int i = 0;
        while(!found && i < l){
            try {
                found = this.__list__.get(i).__eq__(value).__integer__ != 0;
            } catch (Exception e) {
                
            }
        }
        return new __PyInteger(found);
    }
    
    public __PyObject __delitem__(__PyObject index) {
        if(!(index instanceof __PyInteger))
            throw new ArrayIndexOutOfBoundsException("Index must be int object");
        
        return this.__list__.remove(index.__integer__);
    }
    
    public __PyObject __getitem__(__PyObject index) {
        if(!(index instanceof __PyInteger))
            throw new ArrayIndexOutOfBoundsException("Index must be int object");
        int ind = index.__integer__;
        if(ind < 0)
            ind = this.__list__.size() - ind;
        return this.__list__.get(ind);
    }
    
    public __PyObject append(__PyObject value) {
        this.__list__.add(value);
        return this;
    }
    
    public __PyObject index(__PyObject value) {
        boolean found = false;
        int l = this.__list__.size();
        int i = 0;
        int index = -1;
        while(!found && i < l){
            try {
                found = this.__list__.get(i).__eq__(value).__integer__ != 0;
                if(found)
                    index = i;
            } catch (Exception e) {
                
            }
        }
        return new __PyInteger(index);
    }
 
    public __PyObject remove(__PyObject value) throws Exception{
       __PyObject index = this.index(value);
       if(index.__integer__ == -1)
           throw new Exception("Value not in list");
       return this.__delitem__(index);
    }
    
    public __PyObject extend(__PyObject list) throws Exception {
        if(!(list instanceof __PyList))
            throw new Exception("Can extend only by list object");
        __PyList res = new __PyList();
        res.__list__.addAll(this.__list__);
        res.__list__.addAll(list.__list__);
        return res;
    }
    
    public __PyObject __replaceitem(__PyObject index, __PyObject value) throws NotImplementedException{
        if(!(index instanceof __PyInteger))
            throw new ArrayIndexOutOfBoundsException("Index must be int object");
        int ind = index.__integer__;
        if(ind < 0)
            ind = this.__list__.size() - ind;
        __PyObject var = this.__list__.remove(ind);
        this.__list__.add(ind, value);
        return var;
    }
    
    public __PyObject insert(__PyObject index, __PyObject value) throws NotImplementedException{
        if(!(index instanceof __PyInteger))
            throw new ArrayIndexOutOfBoundsException("Index must be int object");
        int ind = index.__integer__;
        if(ind < 0)
            ind = this.__list__.size() - ind;
        this.__list__.add(ind, value);
        return this;
    }
    
    public __PyObject clear() throws NotImplementedException{
        this.__list__.clear();
        return this;
    }
    
    public __PyObject sort() throws Exception{
        __PyList res = new __PyList();
        
        int l = this.__list__.size();
        int num = 0;
        __PyObject tmp;
        for(int i = 0; i < l; i++){
            tmp = this.__list__.get(i);
            int j = 0;
            while(true){
                if(j == num){
                    res.__list__.add(tmp);
                    num++;
                    break;
                }else{
                    if(res.__list__.get(j).__gt__(tmp).__integer__ == 0){
                        res.__list__.add(j, tmp);
                        num++;
                        break;
                    }
                    j++;
                }
            }
        }
        return res;
    }
    
    public __PyObject __len__() throws NotImplementedException{
        return new __PyInteger(this.__list__.size());
    }
    
    public __PyObject __add__(__PyObject value) throws Exception {
        return this.extend(value);
    }
    
    public __PyObject __mul__(__PyObject value) throws Exception {
        if(!(value instanceof __PyInteger))
            throw new ArrayIndexOutOfBoundsException("Can multiply only by int object");
        
        __PyObject res = this;
        for(int i = 1; i < value.__integer__; i++){
            res = res.extend(this);
        }
        return res;
    }
    
    // Equal
    public __PyObject __lt__(__PyObject value) throws Exception {
        if(!(value instanceof __PyList))
            throw new Exception("Can equal only with list object");
        
        int l1 = this.__list__.size();
        int l2 = value.__list__.size();
        
        if(l1 != l2){
            if(l1 < l2)
                return new __PyInteger(true);
            return new __PyInteger(false);
        }
            
        
        for(int i = 0; i < l1; i++){
            if(this.__list__.get(i).__lt__(value.__list__.get(i)).__integer__ == 0)
                return new __PyInteger(false);
        }
        return new __PyInteger(true);
    }
    
    public __PyObject __le__(__PyObject value) throws Exception {
        if(this.__lt__(value).__integer__ == 1)
            return new __PyInteger(true);
        if (this.__eq__(value).__integer__ == 1)
            return new __PyInteger(true);
        return new __PyInteger(false);
    }
    
    public __PyObject __eq__(__PyObject value) throws Exception  {
        if(!(value instanceof __PyList))
            throw new Exception("Can equal only with list object");
        
        int l1 = this.__list__.size();
        int l2 = value.__list__.size();
        
        if(l1 != l2)
            return new __PyInteger(false);
        
        for(int i = 0; i < l1; i++){
            if(this.__list__.get(i).__eq__(value.__list__.get(i)).__integer__ == 0)
                return new __PyInteger(false);
        }
        return new __PyInteger(true);
    }
    
    public __PyObject __ne__(__PyObject value) throws Exception {
        return new __PyInteger(this.__eq__(value).__integer__ != 1);
    }
    
    public __PyObject __gt__(__PyObject value) throws Exception {
        return new __PyInteger(this.__le__(value).__integer__ != 1);
    }
    
    public __PyObject __ge__(__PyObject value) throws Exception {
        return new __PyInteger(this.__lt__(value).__integer__ != 1);
    }
}

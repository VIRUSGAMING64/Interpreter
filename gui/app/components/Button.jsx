import React from "react"

export default function Button({text, onclick, isicon = true}){
    return <button className={
        isicon ? "w-8 h-8 rounded-full cursor-pointer bg-indigo-700 flex items-center justify-center material-icons text-black" : "text-black saves bg-indigo-800"
        } onClick={onclick}>
        {text}
    </button>

}

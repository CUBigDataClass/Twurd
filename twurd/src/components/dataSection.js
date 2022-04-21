import React, { PureComponent } from 'react'
import {Bar} from './bar'
//https://www.geeksforgeeks.org/how-to-create-a-custom-progress-bar-component-in-react-js/
export const DataSection = ({Primarycolor, progress, word, numTweeted}) =>{
    return (
        <div>
            <div className="dataSectionHeader">
                <div className="word">
                    {word}
                </div>
                <div>
                    Tweeted by {numTweeted} people
                </div>
            </div>
            <Bar Primarycolor={Primarycolor} progress={progress}/>
        </div>
    )

}
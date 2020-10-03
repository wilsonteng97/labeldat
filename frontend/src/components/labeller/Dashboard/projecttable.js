import React from 'react';
import './index.css';
import ReactToolTip from 'react-tooltip'
import { Button } from 'antd';
//temporary file with fake data

class Table extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            projects: [
                {
                    projectname: 'lolxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
                    datecreated: '09 Aug 2020',
                    amtcomplete: 40,
                    taskscount: 200,
                    label: true, review: true
                },
                { projectname: 'ddd', datecreated: '09 Aug 2020', amtcomplete: 41, taskscount: 100, label: true, review: false },
                { projectname: 'ssss', datecreated: '20 Aug 2020', amtcomplete: 40, taskscount: 204, label: false, review: true },
                { projectname: 'qqq', datecreated: '20 Sep 2020', amtcomplete: 80, taskscount: 300, label: true, review: true }
            ],
        }
    }

    renderTableHeader() {
        return (
            <tr>
                <td className="tableheader-style1">Project</td>
                <td className="tableheader-style2">Amount Completed</td>
                <td className="tableheader-style3">Actions</td>
            </tr>)
    }

    renderTableData() {
        return this.state.projects.map((project) => {
            const { projectname, datecreated, amtcomplete, taskscount, label, review } = project
            return (
                <tr key={projectname}>
                    <td className="tablecontent-style1" data-for='custom-color' data-tip={"Date Created: " + datecreated}>
                        <ReactToolTip className="hover-style" id='custom-color' place='right' border
                            textColor='#fff' backgroundColor='#00B7E0' borderColor='#00B7E0' />{projectname}</td>
                    <td className="tablecontent-style2" data-for='custom-color' data-tip={((amtcomplete / 100) * taskscount).toFixed(0)
                        + "/" + taskscount + " Tasks Done"}>
                        {amtcomplete + "%"}</td>
                    {this.renderButtons(label, review)}
                </tr>
            )
        })
    }

    renderButtons(label, review) {
        let labelbutton;
        let reviewbutton;
        if (label) {
            labelbutton = <Button className="button-style"> Label </Button>;
        } else {
            labelbutton = <Button className="button-style" disabled="true"> Label </Button>;
        }
        if (review) {
            reviewbutton = <Button className="button-style"> Review </Button>;
        }
        else {
            reviewbutton = <Button className="button-style" disabled="true"> Review </Button>;
        }
        return (
            <td className="tablecontent-style3">
                <td>{labelbutton}</td>
                <td style={{ paddingLeft: '10px' }}>{reviewbutton}</td>
            </td>
        )
    }

    render() {
        return (
            <div>
                <table id='projects'>
                    <tbody>
                        <tr>{this.renderTableHeader()}
                        </tr>
                        <tr>{this.renderTableData()}</tr>
                    </tbody>
                </table>
            </div>
        )
    }
}

export default Table 
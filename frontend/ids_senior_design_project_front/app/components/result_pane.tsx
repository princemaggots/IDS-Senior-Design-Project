import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { 
    ResultTableRows, 
    ModelSubResultTableRows, 
    ClassSubResultTableRows, 
} from '../../script/seed';

export default function ResultPane(data: any, algorithm: string) {
    console.log(algorithm);
    return (
        <div className='flex gap-10 mt-6'>
            <div className='flex flex-col w-3/4'>
                <h1 className='mb-5'>{algorithm}</h1>
                <div className='flex gap-10'>
                    <TableContainer component={Paper}>
                        <Table sx={{ minWidth: 650 }} aria-label="simple table">
                            <TableHead>
                                <TableRow>
                                    <TableCell>Attack Class</TableCell>
                                    <TableCell align="right">Precision</TableCell>
                                    <TableCell align="right">Recall</TableCell>
                                    <TableCell align="right">F1 Score</TableCell>
                                    <TableCell align="right">Support</TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                            {ResultTableRows.map((row) => (
                                <TableRow
                                key={row.attackClass}
                                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                                >
                                <TableCell component="th" scope="row">
                                    {row.attackClass}
                                </TableCell>
                                <TableCell align="right">{row.precision}</TableCell>
                                <TableCell align="right">{row.recall}</TableCell>
                                <TableCell align="right">{row.f1}</TableCell>
                                <TableCell align="right">{row.support}</TableCell>
                                </TableRow>
                            ))}
                            </TableBody>
                        </Table>
                    </TableContainer>
                    {/* <TableContainer component={Paper}>
                        <Table aria-label="simple table">
                            <TableHead>
                                <TableRow>
                                    <TableCell>Evaluation Matrix</TableCell>
                                    <TableCell >Value</TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                            {ModelSubResultTableRows.map((row) => (
                                <TableRow
                                key={row.evaluationMatrix}
                                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                                >
                                <TableCell component="th" scope="row">
                                    {row.evaluationMatrix}
                                </TableCell>
                                <TableCell >{row.value}</TableCell>
                                </TableRow>
                            ))}
                            </TableBody>
                        </Table>
                    </TableContainer> */}
                </div>
            </div>
            <div className='w-1/4'>
                <h1 className='mb-5'>F1 for each type of attack class</h1>
                <TableContainer component={Paper}>
                    <Table aria-label="simple table">
                        <TableHead>
                            <TableRow>
                                <TableCell>Attack Class</TableCell>
                                <TableCell >Value</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                        {ClassSubResultTableRows.map((row) => (
                            <TableRow
                            key={row.attackClass}
                            sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                            >
                            <TableCell component="th" scope="row">
                                {row.attackClass}
                            </TableCell>
                            <TableCell >{row.value}</TableCell>
                            </TableRow>
                        ))}
                        </TableBody>
                    </Table>
                </TableContainer>
            </div>
        </div>
    )
}

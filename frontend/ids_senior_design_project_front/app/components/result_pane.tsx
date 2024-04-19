import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

export default function ResultPane({data, pastData, selected }: {data: any, pastData?: any, selected: boolean }) {
    return (
        <div className='flex flex-col gap-10 mt-6'>
            <div className='flex flex-col w-3/4'>
                <h1 className='mb-5'><strong>{data.model}</strong></h1>
                <div className='flex flex-col gap-10'>
                    <TableContainer component={Paper}>
                        <Table sx={{ minWidth: 650 }} aria-label="simple table">
                            <TableHead>
                                <TableRow>
                                    <TableCell>Accuracy</TableCell>
                                    <TableCell align="right">Precision</TableCell>
                                    <TableCell align="right">Recall</TableCell>
                                    <TableCell align="right">F1 Score</TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                            <TableRow
                            sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                            >
                            <TableCell component="th" scope="row">{data.acc_score}</TableCell>
                            <TableCell align="right">{data.prec_score}</TableCell>
                            <TableCell align="right">{data.rec_score}</TableCell>
                            <TableCell align="right">{data.f1}</TableCell>
                            </TableRow>
                            </TableBody>
                        </Table>
                    </TableContainer>
                    {selected && pastData && (
                        <TableContainer component={Paper}>
                            <Table sx={{ minWidth: 650 }} aria-label="simple table">
                            <TableHead>
                                <TableRow>
                                <TableCell>Accuracy</TableCell>
                                <TableCell align="right">Precision</TableCell>
                                <TableCell align="right">Recall</TableCell>
                                <TableCell align="right">F1 Score</TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                <TableRow
                                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                                >
                                <TableCell component="th" scope="row">{pastData.acc_score}</TableCell>
                                <TableCell align="right">{pastData.prec_score}</TableCell>
                                <TableCell align="right">{pastData.rec_score}</TableCell>
                                <TableCell align="right">{pastData.f1}</TableCell>
                                </TableRow>
                            </TableBody>
                            </Table>
                        </TableContainer>
                        )}
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
            <div className='flex gap-10'>
                <div className='w-1/2'>
                    <h1 className='mb-5'><strong>F1 for each type of attack class</strong></h1>
                    <TableContainer component={Paper}>
                        <Table aria-label="simple table">
                            <TableHead>
                                <TableRow>
                                    <TableCell>Attack Class</TableCell>
                                    <TableCell >Value</TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                            {data.class_f1.map((row: any) => (
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
                <div className='w-1/2'>
                    {selected && pastData && (<>
                        <h1 className='mb-5'><strong>F1 for each type of attack class(prev)</strong></h1>
                        <TableContainer component={Paper}>
                            <Table aria-label="simple table">
                                <TableHead>
                                    <TableRow>
                                        <TableCell>Attack Class</TableCell>
                                        <TableCell >Value</TableCell>
                                    </TableRow>
                                </TableHead>
                                <TableBody>
                                {pastData.class_f1.map((row: any) => (
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
                    </>
                    )}
                </div>
            </div>
            
        </div>
    )
}

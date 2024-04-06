'use client'

import Button from '@mui/material/Button';
import { DataGrid, GridColDef } from '@mui/x-data-grid';
import { rows } from '@/script/seed';
import { usePathname } from 'next/navigation'
import { columns } from '@/app/lib/data';


export default function HistoryTable() {
    const pathname = usePathname()
    const isPastSession = pathname === '/past_session';

    const columnsWithButton: GridColDef[] = [
        ...columns,
        {
            field: 'load-btn',
            headerName: '',
            width: 160,
            sortable: false,
            align: 'center',
            disableColumnMenu: true,
            renderCell: (params) => (
                <Button variant="contained" className='bg-primary'onClick={() => handleButtonClick(params.row)}>
                    Load
                </Button>
            ),
        },
    ];
    
    function handleButtonClick(row: any) {
        console.log(row)
    }

    return (
        <div className='w-full h-[371px] flex justify-center'>
            <DataGrid
                rows={rows} 
                columns={isPastSession ? columnsWithButton : columns}
                disableRowSelectionOnClick
                initialState={{
                    pagination: {
                        paginationModel: { page: 0, pageSize: 5 },
                    },
                }}
            />
        </div>
    )
};
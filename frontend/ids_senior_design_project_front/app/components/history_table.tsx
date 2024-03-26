'use client'

import { DataGrid } from '@mui/x-data-grid';
import { columns, rows} from '@/script/seed';

export default function HistoryTable() {
    return (
        <DataGrid
            rows={rows}
            columns={columns}
            initialState={{
                pagination: {
                    paginationModel: { page: 0, pageSize: 5 },
                },
            }}
            pageSizeOptions={[5, 10]}
        />
    )
};
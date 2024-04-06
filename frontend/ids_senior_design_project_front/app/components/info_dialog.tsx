import InfoOutlinedIcon from '@mui/icons-material/InfoOutlined';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import Paper from '@mui/material/Paper';
import { useState } from 'react';
import Draggable from 'react-draggable';
import { DialogProps } from '../lib/definitions';

function PaperComponent(props: any) {
    return (
        <Draggable
        handle="#draggable-dialog-title"
        cancel={'[class*="MuiDialogContent-root"]'}
        >
        <Paper {...props} />
        </Draggable>
    );
}

export default function InfoDialog({prop_name, prop_description}: DialogProps) {
    const [open, setOpen] = useState(false);

    const handleOpen = (event: React.MouseEvent<HTMLButtonElement>) => {
        event.preventDefault()
        setOpen((prevState) => !prevState);
    };

    return (
        <>
            <button onClick={handleOpen} >
                <InfoOutlinedIcon style={{ width: '1rem', height: '1rem' }} className='ml-auto text-gray-400 hover:text-black transition-colors duration-300'/>
            </button>
            <Dialog
                open={open}
                onClose={handleOpen}
                PaperComponent={PaperComponent}
                aria-labelledby="draggable-dialog-title"
            >
                <DialogTitle style={{ cursor: 'move' }} id="draggable-dialog-title">
                    {prop_name}
                    </DialogTitle>
                        <DialogContent>
                            <DialogContentText>
                                {prop_description} 
                            </DialogContentText>
                        </DialogContent>
                    <DialogActions>
                    <Button autoFocus onClick={handleOpen}>
                        Close
                    </Button>
                </DialogActions>
            </Dialog>
        </>
    );
}
'use client'

import { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import LinearProgress from '@mui/material/LinearProgress';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import { LinerProgressProp } from '../lib/definitions';

function LinearProgressWithLabel({value}: LinerProgressProp) {
    return (
        <Box sx={{ display: 'flex', alignItems: 'center' }}>
        <Box sx={{ width: '100%', mr: 1 }}>
            <LinearProgress variant="determinate" value={value} />
        </Box>
        <Box sx={{ minWidth: 35 }}>
            <Typography variant="body2" color="text.secondary">{`${Math.round(
                value,
            )}%`}</Typography>
        </Box>
        </Box>
    );
}

LinearProgressWithLabel.propTypes = {
    value: PropTypes.number.isRequired,
};

export default function LinearWithValueLabel() {
    const [progress, setProgress] = useState(10);

    useEffect(() => {
        const timer = setInterval(() => {
        setProgress((prevProgress) => (prevProgress >= 100 ? 10 : prevProgress + 10));
        }, 800);
        return () => {
        clearInterval(timer);
        };
    }, []);

    return (
        <Box sx={{ width: '100%' }}>
        <LinearProgressWithLabel value={progress} />
        </Box>
    );
}


import LinearWithValueLabel from '@/app/components/linear_progress';
import CircularIndeterminate from '@/app/components/circular_indeterminate';

export default function page(){
    return (
        <div>
            <p className="text-xl">Execution</p>
            <LinearWithValueLabel />
            <CircularIndeterminate />
        </div>
    );
}
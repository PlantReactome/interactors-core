package org.reactome.server.interactors.exception;

/**
 * Exception thrown when trying to Query PSICQUIC
 * PSICQUIC Registry shows the service is up and running
 * but we can't query this particular server.
 *
 * @author Guilherme S Viteri <gviteri@ebi.ac.uk>
 */
public class PsicquicQueryException extends Exception {

    public PsicquicQueryException(String message) {
        super(message);
    }

    public PsicquicQueryException(Throwable cause) {
        super(cause);
    }
}
